
 <h4 style='color:red'>Python的学习中</h4> 

```
*  1.pip安装慢使用[豆瓣源](https://pypi.douban.com/simple/)
*  2.Flask的框架：
  *  装饰器中的return{}容易出错:
            @home.context_processor
            def my_context_processor():
                  if hasattr(g,'user'):
                    return {'user':g.user}
                  return {}       

```
