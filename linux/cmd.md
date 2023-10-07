[toc]

# cat		
    -n 加行号(空行也算1行)  
    -b 加行号(空行不算一行)  
    -s 压缩连续的空行
	-A 显示回车$ (mac是-b) 
    -e 显示行结束符$

# tac a.txt 	
    #多行反向显示

# rev 		
    #在一行里reverse 显示

# more

# less		
    #分页显示

# head	-n 3	
    #显示文件的头，默认前十行, -n 3前3行

# tail -n 3 	
        #显示文件的尾，默认后十行, -n 3前3行
		#正在变化的文件，要跟踪文件新追加的内容的话, 就 **tail -f /data/f2.log**, 有追加内容的话就能看到
		# -F: 跟踪文件名，相当于—follow=name —retry , 如果文件被删了，会显示
		# no such file or directory, -f 就不会

# date		
    #显示今天的日期. 

# date -d ‘-1 day’	
    #显示昨天的日期

# cut		
        # 按列抽取文本
		# -d DELIMITER：指明分隔符，默认tab
		# -f  FIELDS: 
		# -c 按字符数切割
		# 以:为分隔符，1,3,5,6,7列，取出系统中所有用户的用户名和uid
        # **cut -d: -f 1,3,5-7 /etc/passwd**
		# cut -c1-9	按1-9个字符切割
# paste	
        合并两个文件同行号的列到一行
		paste [option]… [file]…
		-d 分隔符：指定分隔符，默认用TAB
		-s 所有行合成一行显示
		paste f1 f2
		paste -s f1 f2	  # f1文件里的所有行合成一行，f1文件里的所有行合成另一行

# wc
        # 显示文件有几行，几个单词，几个字节
		# 经常和管道一起用
		# 统计当前目录下文件的个数 ls | wc
		# -l 统计多少行 lines ; -c bytes ; -m chars; -w words
		$ wc story.txt
		  39   237    1901
		  行数  字数   字节数
		# 这个文件有几行就表示有多少次用户访问过
		$ cat /var/log/https/access_log | wc -l	

# sort
        # 把整理过的文本显示在STDOUT, 不改变原始文件
        # -r 反方向整理
        # -R 随机排序
        # -u 选项（unique)删除输出中的重复行
        # -n 执行按数字大小整理
        # -t c 选项使用c做为字段界定符
        # -k X  选项按照使用c字符分割的X列来整理能够使用多次
        # -f 忽略fold字符串中的字符大小写

        # 对/etc/passwd第三列排序
        # -t: 以:作为分隔符 , -k3 第三列
        # 默认按字符排序 -n 按照数字排序
        $ sort -t: -k3 -n /etc/passwd

        # 找到分区利用率最大的数字
        $ df | tr -s ‘ ‘ % | cut -d% -f5 | sort -nr | head -n1

        # 抽签
        $ seq 102 | sort -R | head -n1	

# uniq
        # 从输入中删除前后相接的重复的行
        # -c 显示每行重复出现的次数
        # -d 仅显示重复过的行
        # -u 仅显示不曾重复的行
        # cat a.txt | sort | uniq -c    显示每行重复的次数

# diff
        # 命令的输出被保存在一种叫做“补丁”的文件中
        # -u unified
# patch
        # 复制在其他文件中进行的改变（careful when use）
        # -b 自动备份改变了的文件
        # diff -u foo.conf foo2.conf > foo.patch
        # patch -b foo.conf foo.patch
        # -b 先把foo.conf做个备份maybe foo.conf.ibak, 然后在foo.conf里进行改变







