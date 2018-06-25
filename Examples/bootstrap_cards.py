
from pyno import HTML as H
from flask import Flask

app = Flask(__name__)


@H.construct
def imageCell():
    return """
<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<section>
<div class="container">
<div class="row">
    <div class="col">
        <div class="container py-3">
        <div class="card">
          <div class="row ">
            <div class="col-md-4">
                <img src="https://placeholdit.imgix.net/~text?txtsize=20&txt=80%C3%9780&w=80&h=80" class="w-100">
              </div>
              <div class="col-md-8 px-3">
                <div class="card-block px-3">
                  <h4 class="card-title">Lorem ipsum dolor sit amet</h4>
                  <p class="card-text">Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
                </div>
              </div>
            </div>
          </div>
        </div>
                <div class="container py-3">
        <div class="card">
          <div class="row ">
            <div class="col-md-4">
                <img src="https://placeholdit.imgix.net/~text?txtsize=20&txt=80%C3%9780&w=80&h=80" class="w-100">
              </div>
              <div class="col-md-8 px-3">
                <div class="card-block px-3">
                  <h4 class="card-title">Lorem ipsum dolor sit amet</h4>
                  <p class="card-text">Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
                </div>
              </div>
            </div>
          </div>
        </div>
    </div>
    <div class="col">
        <div class="container py-3">
        <div class="card">
          <div class="row ">
            <div class="col-md-4">
                <img src="https://placeholdit.imgix.net/~text?txtsize=20&txt=80%C3%9780&w=80&h=80" class="w-100">
              </div>
              <div class="col-md-8 px-3">
                <div class="card-block px-3">
                  <h4 class="card-title">Lorem ipsum dolor sit amet</h4>
                  <p class="card-text">Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
                </div>
              </div>
            </div>
          </div>
        </div>
                <div class="container py-3">
        <div class="card">
          <div class="row ">
            <div class="col-md-4">
                <img src="https://placeholdit.imgix.net/~text?txtsize=20&txt=80%C3%9780&w=80&h=80" class="w-100">
              </div>
              <div class="col-md-8 px-3">
                <div class="card-block px-3">
                  <h4 class="card-title">Lorem ipsum dolor sit amet</h4>
                  <p class="card-text">Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
                </div>
              </div>
            </div>
          </div>
        </div>        
    </div>
</div>
</section>
"""

"""
<div class="container py-3">
    <div class="card">
      <div class="row ">
        <div class="col-md-2">
            <img src="https://placeholdit.imgix.net/~text?txtsize=38&txt=400%C3%97400&w=60&h=60" class="w-100">
          </div>
          <div class="col-md-4 px-3">
            <div class="card-block px-3">
              <h4 class="card-title">Lorem ipsum dolor sit amet</h4>
              <p class="card-text">Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
              <p class="card-text">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
              <a href="#" class="btn btn-primary">Read More</a>
            </div>
          </div>
        </div>
      </div>
    </div>
"""

app.route('/')(imageCell)

if __name__ == '__main__':
    app.run(debug=True)