import scipy.constants as c
import numpy as np


def spherical_to_cartesian(r, theta, phi):
    x = (r * np.sin(theta) * np.cos(phi))
    y = (r * np.sin(theta) * np.sin(phi))
    z = (r * np.cos(theta))
    return (x, y, z)


def cartesian_to_spherical(x, y, z):
    r = ((x*x + y*y + z*z)**0.5)
    if z == 0:
        theta = 0
    elif z != 0:
        theta = (np.arctan((x*x + y*y)**0.5 / z))
    if x == 0:
        phi = c.pi/2
    else:
        phi = (np.arctan(y/x))
    return (r, theta, phi)


def radial_wave_func(n, l, r):
    a = c.physical_constants['Bohr radius'][0]
    if n == 1:
        ans = 2*np.exp(-r/a)
    if n == 2:
        if l == 0:
            ans = (1/np.sqrt(2))*(1-r/(2*a))*np.exp(-r/(2*a))
        if l == 1:
            ans = (1/np.sqrt(24))*(r/(a))*np.exp(-r/(2*a))
    if n == 3:
        if l == 0:
            ans = (2/(81*np.sqrt(3)))*(27-(18*r/a)+2*(r/a)**2)*np.exp(-r/(3*a))
        if l == 1:
            ans = (8/(27*np.sqrt(6)))*(1-r/(6*a))*(r/a)*np.exp(-r/(3*a))
        if l == 2:
            ans = (4/(81*np.sqrt(30)))*((r/a)**2)*np.exp(-r/(3*a))
    if n == 4:
        if l == 0:
            ans = (1/4)*(1-(3/4*r/a)+1/8*(r/a)**2 -
                         1/192*(r/a)**3)*np.exp(-r/(4*a))
        if l == 1:
            ans = (np.sqrt(5)/(16*np.sqrt(3))) * \
                (1-1/4*r/a+1/80*(r/a)**2)*(r/a)*np.exp(-r/(4*a))
        if l == 2:
            ans = (1/(64*np.sqrt(5)))*(1-1/12*r/a)*(r/a)**2*np.exp(-r/(4*a))
        if l == 3:
            ans = (1/(768*np.sqrt(35)))*(r/a)**3*np.exp(-r/(4*a))
    return np.complex(ans)


def angular_wave_func(m, l, theta, phi):
    if l == 0:
        ans = np.sqrt(1/(4*c.pi))
    if l == 1:
        if m == 1:
            ans = -1 * np.sqrt(3/(8*c.pi))*np.sin(theta)*np.exp(1j*phi)
        if m == 0:
            ans = np.sqrt(3/(4*c.pi))*np.cos(theta)
        if m == -1:
            ans = np.sqrt(3/(8*c.pi))*np.sin(theta)*np.exp(-1j*phi)
    if l == 2:
        if m == 2:
            ans = np.sqrt(15/(32*c.pi))*(np.sin(theta))**2*np.exp(1j*2*phi)
        if m == 1:
            ans = -1*np.sqrt(15/(8*c.pi))*np.cos(theta) * \
                np.sin(theta)*np.exp(1j*phi)
        if m == 0:
            ans = np.sqrt(5/(16*c.pi))*(3*(np.cos(theta))**2-1)
        if m == -1:
            ans = np.sqrt(15/(8*c.pi))*np.cos(theta) * \
                np.sin(theta)*np.exp(-1j*phi)
        if m == -2:
            ans = np.sqrt(15/(32*c.pi))*(np.sin(theta))**2*np.exp(-1j*2*phi)
    if l == 3:
        if m == 3:
            ans = -1*np.sqrt(35/(64*c.pi))*(np.sin(theta))**3*np.exp(1j*3*phi)
        if m == 2:
            ans = np.sqrt(105/(32*c.pi))*np.cos(theta) * \
                (np.sin(theta))**2*np.exp(1j*2*phi)
        if m == 1:
            ans = -1*np.sqrt(21/(64*c.pi))*np.sin(theta) * \
                (5*(np.cos(theta))**2-1)*np.exp(1j*phi)
        if m == 0:
            ans = np.sqrt(7/(16*c.pi))*(5*(np.cos(theta))**3-3*np.cos(theta))
        if m == -1:
            ans = np.sqrt(21/(64*c.pi))*np.sin(theta) * \
                (5*(np.cos(theta))**2-1)*np.exp(-1j*phi)
        if m == -2:
            ans = np.sqrt(105/(32*c.pi))*np.cos(theta) * \
                (np.sin(theta))**2*np.exp(-1j*2*phi)
        if m == -3:
            ans = np.sqrt(35/(64*c.pi))*(np.sin(theta))**3*np.exp(-1j*3*phi)
    return np.complex(ans)
#    return np.complex(np.round(ans, 5))


def mgrid3d(xstart, xend, xpoints, ystart, yend, ypoints, zstart, zend, zpoints):
    xinterval = (xend - xstart) / (xpoints - 1)
    yinterval = (yend - ystart) / (ypoints - 1)
    zinterval = (zend - zstart) / (zpoints - 1)
    num_rows = ypoints
    num_col = zpoints
    num_mat = xpoints

    mgrid = []
    x = []
    val = xstart
    for mat in range(num_mat):
        ans = []
        for row in range(num_rows):
            row = []
            for col in range(num_col):
                row.append(np.round(val, 5))
            ans.append(row)
        val += xinterval
        x.append(ans)
    mgrid.append(x)

    y = []
    for mat in range(num_mat):
        ans = []
        val = ystart
        for row in range(num_rows):
            row = []
            for col in range(num_col):
                row.append(np.round(val, 5))
            ans.append(row)
            val += yinterval
        y.append(ans)
    mgrid.append(y)

    z = []
    for mat in range(num_mat):
        ans = []
        for row in range(num_rows):
            row = []
            val = zstart
            for col in range(num_col):
                row.append(np.round(val, 5))
                val += zinterval
            ans.append(row)
        z.append(ans)
    mgrid.append(z)

    return np.array(mgrid)


a = c.physical_constants['Bohr radius'][0]
#a = mgrid3d(-8,8,2,-8,8,2,-8,8,2)
#print(a[0],a[1],a[2])


def phy(n, l, m, x, y, z):

    r, theta, phi = cartesian_to_spherical(x, y, z)
    r = r*a
    yl = angular_wave_func(m, l, theta, phi)
    print(yl)
    ylop = angular_wave_func(-m, l, theta, phi)
    if m < 0:
        ylm = (1j/np.sqrt(2))*(yl-(-1)**m*ylop)
    elif m == 0:
        ylm = yl
    elif m > 0:
        ylm = (1/np.sqrt(2))*(ylop+(-1)**m*yl)
    rnl = radial_wave_func(n, l, r)
    phy = np.round(ylm * rnl, 5)
    magphy = np.round(np.sqrt(phy.real ** 2 + phy.imag ** 2), 5)
    magphysquare = magphy ** 2
    return np.round(magphysquare, 5)


def hydrogen_wave_func(n, l, m, roa, Nx, Ny, Nz):
    coor = mgrid3d(-roa, roa, Nx, -roa, roa, Ny, -roa, roa, Nz)
    x = coor[0]
    y = coor[1]
    z = coor[2]
    phy_v = np.vectorize(phy)
    magi = phy_v(n, l, m, x, y, z)
    return x, y, z, magi
