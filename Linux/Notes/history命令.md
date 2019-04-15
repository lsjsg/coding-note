# history命令

### 参数

`-c`（清空所有历史命令）

`-d` （删除历史命令中指定的第offset条命令）

`-a`（追加本次会话中的新执行的命令历史列表到历史文件）

`-n`（读取历史文件中未读过的行到命令历史列表）

`-r`（读取历史文件到历史列表）

`-w`（保存历史列表到指定的历史文件）

`-p`（展开历史参数成多行，但不存在历史列表中）

`-s`（展开历史参数成一行，附加在历史列表后）

### 执行上一条命令四种方式

1. 方向上键并回车
2. `!!` 并回车
3. Ctrl + p 并回车执行
4. `!:0` 执行前一条命令(去除参数)

### 其他快捷方式

`Ctrl + n` 显示当前历史中的下一条命令，但不执行

`!n` 执行history命令输出对应序号n的命令

`!-n` 执行history历史中倒数第n个命令

`!string` 重复前一个以“string”开头的命令

`!?string` 重复前一个包含string的命令

使用up（向上）和down（向下）键来上下浏览从前输入的命令

`ctrl + r` 来在命令历史中搜索命令（reverse-i-search）：

`Ctrl + g`：从历史搜索模式退出 

### 与命令历史相关的环境变量

`HISTSIZE`：命令历史记录的条数

`HISTFILE`：指定历史文件，默认为~/.bash_history

`HISTFILESIZE`：命令历史文件记录历史的条数

`HISTTIMEFORMAT=“%F %T“` 显示时间

`HISTIGNORE=“str1:str2:… “` 忽略string1,string2历史

控制命令历史的记录方式：

环境变量：`HISTCONTROL`

`ignoredups` 默认，忽略重复的命令，连续且相同为“重复”

`ignorespace` 忽略所有以空白开头的命令

`ignoreboth` 相当于`ignoredups`, `ignorespace`的组合

`erasedups` 删除重复命令

`export` 变量名=”值“

history命令相关的配置文件存放在 `/etc/profile` 或 `~/.bash_profile`，更改之后永久有效