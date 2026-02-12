from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'

# Enable caching for static files
@app.after_request
def add_header(response):
    if 'text/html' not in response.content_type:
        # Cache static files for 1 year
        response.cache_control.max_age = 31536000
        response.cache_control.public = True
    else:
        # Cache HTML for 1 hour
        response.cache_control.max_age = 3600
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            phone = request.form.get('phone')
            message = request.form.get('message')
            
            # For now, just return success
            # You can add email sending functionality later
            return jsonify({'success': True, 'message': 'Message sent successfully!'})
            
        except Exception as e:
            return jsonify({'success': False, 'message': 'Failed to send message. Please try again.'})
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
