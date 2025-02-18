/* Generated {{ now_iso_8601() }} */
{% if logo_adornment and path_exists('app/static/logo-adornments/' + logo_adornment + '.min.js') %}
import "{{ url_for('static', filename='logo-adornments/' + logo_adornment + '.min.js') }}";
{% else %}
/* No logo adornments available */
{% endif %}
