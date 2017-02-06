#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


class Pager(object):
    def __init__(self,current_page):
        self.current_page=int(current_page)
    @property
    def start(self):
        return (self.current_page-1)*10
    @property
    def end(self):
        return self.current_page*10

    def page_str(self,all_item,base_url):
         all_page,div=divmod(all_item,10)
         if div >0:
            all_page +=1

         pager_list=[]
         if all_page < 11:
             start = 1
             end = all_page
         else:
             if self.current_page <= 6:
                 start = 1
                 end = 12
             else:
                 start = self.current_page - 5
                 end = self.current_page+6

                 if self.current_page + 6 > all_page:
                     start = all_page-11
                     end = all_page+1

         for i in range(start,end):
            if i == self.current_page:
                temp="<a style='color:red;font-size:26px; ' href=%s%d>%d</a>"%(base_url,i,i)
            else:
                temp="<a href=%s%d>%d</a>"%(base_url,i,i)

            pager_list.append(temp)

         #上一页
         if self.current_page >1:
            pre_page="<a href=%s%d>上一页</a>"%(base_url,self.current_page-1)
         else:
            pre_page="<a href='javascripts:void(0)'>上一页</a>"
         #下一页
         if self.current_page >= all_page:
            next_page = "<a href='javascripts:void(0)'>上一页</a>"
         else:
             next_page = "<a href=%s%d>下一页</a>"%(base_url,self.current_page+1)

         pager_list.insert(0,pre_page)
         pager_list.append(next_page)

         return "".join(pager_list)