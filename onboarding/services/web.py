from onboarding.models import Profile

def register_web_endpoint(app):
  @app.route(u'/')
  def index():
    return 'index.html'
