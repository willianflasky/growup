
## GIT常用执令说明

*   初始化git项目
>   git init

*   查看当前目录状态
>   git status

*   把代码提交到stage区
>   git add file.txt

>   git add .

*   从stage区提交代码到仓库
> git commit -m "说明"

*   查看commit日志
>   git log

>   git log --pretty=oneline

*   查看提交，回滚所有操作
>   git reflog


*   回滚到上一个版本
>   git reset --hard HEAD^


*   回滚到上二个版本
>   git reset --hard HEAD^^

*   回滚到指定版本
>   git reset --hard afa3kf

*   删除文件
>   git rm file.txt

>   git commit -m "del file.txt"

*   从stage区删除
>   git add test.txt

>   git reset test.txt

*   文件放弃修改
>   git checkout -- file.txt


*   增加远程GIT
>   git remote add origin https://github.com/willianflasky/s16day21.git


####    关联GITHUB
==本地无项目文件==
```
echo "# mysite" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:willianflasky/mysite.git
git push -u origin master

```
==本地有项目文件==
```

git remote add origin git@github.com:willianflasky/mysite.git
git push -u origin master

```

#### 备注

    1.两种方式：https and git
	    2.本地生成公钥添加到GITHUB
		    
		
		*   .gitignore
		>   https://github.com/github/gitignore
		
		*   保存工作区临时地方
		>   git stash   
		
		>   git stash list
		
		>   git stash apply
		
		>   git stash drop
		
		>   git stash pop
		
		
		
		*   分支
		```
		git branch dev          #创建分支
		git checkout dev        #切换到dev分支
		
		git checkout -b dev     #切换到dev分支，如果没有这个分支则创建
		
		git pull origin master  #换取远程master主干代码
		
		git merge dev           #将当前分支合并dev分支
		
		```
		
#### ==合并分支套路==
		```
		    1.git checkout master       #切换到master
			2.git pull                  #拉取远程最新master代码
			3.git merge dev             #在master分支上合并dev分支
			4.push push origin master   #把合并后的代码push到远程master
		```
						""""""""

