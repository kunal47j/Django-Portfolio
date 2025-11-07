import os
from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, current_app, flash
import smtplib
from email.message import EmailMessage

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Read email settings from environment
    EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
    EMAIL_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_PASS = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() in ('true', '1', 'yes')
    EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', 'False').lower() in ('true', '1', 'yes')

    try:
        msg = EmailMessage()
        msg['Subject'] = 'New message from portfolio site'
        # Use the configured email as the sender when available; otherwise use user's email
        if EMAIL_USER:
            msg['From'] = EMAIL_USER
            # set Reply-To so replies go to the visitor
            msg['Reply-To'] = email or EMAIL_USER
            msg['To'] = EMAIL_USER
        else:
            # no configured mailbox — send a message using visitor email as from/to
            msg['From'] = email or 'noreply@example.com'
            msg['To'] = email or 'noreply@example.com'

        msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

        # Choose SSL vs STARTTLS depending on configuration
        if EMAIL_USE_SSL or EMAIL_PORT == 465:
            server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT, timeout=10)
        else:
            server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT, timeout=10)
        server.ehlo()
        if not EMAIL_USE_SSL and EMAIL_USE_TLS:
            server.starttls()
            server.ehlo()

        if EMAIL_USER and EMAIL_PASS:
            server.login(EMAIL_USER, EMAIL_PASS)

        server.send_message(msg)
        server.quit()
        flash('Message sent successfully.', 'success')
        current_app.logger.info('Contact form message sent to %s', EMAIL_USER or email)
    except Exception as e:
        # log and flash error
        current_app.logger.exception('Failed to send contact message')
        flash('Failed to send message. ' + str(e), 'error')

    return redirect(url_for('main.index'))

@bp.route('/resume')
def resume():
    # serve resume from static/media if available
    media_dir = os.path.join(current_app.static_folder, 'media')
    filename = 'Kunal_Resume.pdf'
    # try a few likely names
    candidates = ['Kunal_Resume.pdf', 'Kunal_Resume.pdf', 'Kunal_Resume_1.pdf', 'Kunal_Resume.pdf']
    for f in candidates:
        if os.path.exists(os.path.join(media_dir, f)):
            return send_from_directory(media_dir, f, as_attachment=True)
    return ("Resume not found", 404)
