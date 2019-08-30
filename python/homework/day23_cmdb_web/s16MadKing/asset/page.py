class PageInfo(object):
    def __init__(self, current_page, per_age_num, all_count, base_url, page_range=11):
        """
        :param current_page: 当前页
        :param per_age_num: 每页显示数据条数
        :param all_count: 数据库总个数
        :param base_url: 页码标签的前缀
        :param page_range: 页码个数
        :return: 列表-->str
        """
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = 1
        self.current_page = current_page
        self.per_page_num = per_age_num
        self.all_count = all_count
        a, b = divmod(all_count, per_age_num)
        if b != 0:
            self.all_page = a + 1
        else:
            self.all_page = a

        self.base_url = base_url
        self.page_range = page_range

    def start(self):
        return (self.current_page - 1) * self.per_page_num

    def end(self):
        return self.current_page * self.per_page_num

    def page_str(self):
        """
        :return: list --> str
        """
        page_list = []

        first_page = "<a href='%s?p=%s'>首页</a>" % (self.base_url, 1)
        page_list.append(first_page)

        if self.current_page <= 1:
            prev = "<a href='#'>上一页</a>"
        else:
            prev = "<a href='%s?p=%s'>上一页</a>" % (self.base_url, self.current_page - 1)
        page_list.append(prev)

        # 只有 8页
        if self.all_page <= self.page_range:
            start = 1
            end = self.all_page + 1
        else:
            # 页数 18
            if self.current_page > int(self.page_range / 2):
                # 当前页： 100,101,102
                if (self.current_page + int(self.page_range / 2)) > self.all_page:
                    start = self.all_page - self.page_range + 1
                    end = self.all_page + 1
                # 当前页:  6,7,8,9,10
                else:
                    start = self.current_page - int(self.page_range / 2)
                    end = self.current_page + int(self.page_range / 2) + 1
            else:
                # 当前页： 1,2,3,4,5,
                start = 1
                end = self.page_range + 1

        for i in range(start, end):
            if self.current_page == i:
                temp = '<a class="active" href="%s?p=%s">%s</a>' % (
                    self.base_url, i, i,)
            else:
                temp = '<a href="%s?p=%s">%s</a>' % (
                    self.base_url, i, i,)
            page_list.append(temp)

        if self.current_page >= self.all_page:
            nex = "<a href='#'>下一页</a>"
        else:
            nex = "<a href='%s?p=%s'>下一页</a>" % (self.base_url, self.current_page + 1)
        page_list.append(nex)

        last_page = "<a href='%s?p=%s'>尾页</a>" % (self.base_url, self.all_page)
        page_list.append(last_page)