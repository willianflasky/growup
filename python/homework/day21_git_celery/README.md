###	s16day21 homework

*	git
>	git常用手册.md
*	celery
```
	1.s16day21
		celery.py
		tasks.py
	2.s16day21/mysite	(django + celery)
		启动worker:
		cd ~/s16day21/mysite
		celery -A mysite worker -l info
		启动django
		http://localhost:8000/celery/?a=1&b=20

```
