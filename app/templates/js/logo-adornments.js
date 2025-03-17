/* Generated {{ now_iso_8601() }} by build version {{ app_config.BUILD_VERSION }} */
{% if logo_adornment and static_file_exists('logo-adornments/' + logo_adornment + '.min.js') %}
import "{{ url_for('static', filename='logo-adornments/' + logo_adornment + '.min.js') }}";
{% else %}
/* No logo adornments available */
{% endif %}
