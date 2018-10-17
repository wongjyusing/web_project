import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        context = "Hello, world"
        #self.write(context)
        self.render(template_name='hello.html')

class HelloHandler(tornado.web.RequestHandler):
    def get(self,name):
        context = f"Hello, {name}"
        self.write(context)


class HiHandler(tornado.web.RequestHandler):
    def get(self,name):
        context = f"Hi, {name}"
        #self.write(context)
        self.render(template_name='hi.html',context=context)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r'/hello/(?P<name>[\w-]+)',HelloHandler),
        (r'/hi/(?P<name>[\w-]+)',HiHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
