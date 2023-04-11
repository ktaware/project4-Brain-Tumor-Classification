from flask import Flask, jsonify
app = Flask(__name__)
hello_list = ["<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=495x619>"]
# @app.route("/")
# def home():
#  return "Hi"
# @app.route("/normal")
# def normal():
#  return str(hello_list)

# @app.route("/")
# def template_test():
#     return render_template('home.html', label='', imagesource='file://null')
# @app.route("/pitutary/", methods=['GET', 'POST'])
# def pitutary():
#    return render_template('pitutary.html')
# @app.route("/glioma/", methods=['GET', 'POST'])
# def glioma():
#    return render_template('glioma.html')
# @app.route("/meningioma/", methods=['GET', 'POST'])
# def meningioma():
#    return render_template('meningioma.html')
# @app.route("/page/", methods=['GET', 'POST'])
# def page():
#    return render_template('page.html')
@app.route("/jsonified")
def jsonified_list():
 return jsonify(hello_list)