/* Generated {{ now_iso_8601() }} */
{% if logo_adornment and static_file_exists('logo-adornments/' + logo_adornment + '.min.js') %}
import "{{ url_for('static', filename='logo-adornments/' + logo_adornment + '.min.js') }}";
{% else %}
/* No logo adornments available */
{% endif %}
