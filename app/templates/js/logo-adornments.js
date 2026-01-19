/* Generated {{ now_iso_8601() }} by build version {{ app_config.BUILD_VERSION }} */
{% if logo_adornment %}
{% if static_file_exists('logo-adornments/' + logo_adornment + '.min.js') %}
import "{{ url_for('static', filename='logo-adornments/' + logo_adornment + '.min.js') }}";
{% endif %}
{% if logo_adornment_description %}
document.querySelectorAll(".tna-logo--adornable").forEach(($logo) => {
    const $logoWrapper = $logo.closest("a[href][title]");
    const logoTitle = $logoWrapper.getAttribute("title") || "";
    const logoTitleSuffix = "{{ logo_adornment_description }}";
    $logoWrapper.setAttribute("title", logoTitle ? `${logoTitle} (${logoTitleSuffix})` : logoTitleSuffix);
});
{% endif %}
{% else %}
/* No logo adornments available */
{% endif %}
