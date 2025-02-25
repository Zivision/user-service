import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return "Hello, world!"

    @cherrypy.expose
    def about(self):
        return "This is a simple example of a CherryPy application."

if __name__ == '__main__':
    cherrypy.quickstart(Root(), "/")