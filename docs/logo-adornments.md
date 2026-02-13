# Logo adornments

Adornments can be added to logos in both the [header](https://nationalarchives.github.io/design-system/components/header/) and [global header](https://nationalarchives.github.io/design-system/components/global-header/) components.

## CSS

There is a single entry file ([/enrichment/css/logo-adornments.css](http://localhost:65529/enrichment/css/logo-adornments.css)) that dynamically imports the relevant adornment based on the current date.

These adornments can be included on any service that uses the components from TNA Frontend by including the CSS in the header:

```html
<link
  rel="stylesheet"
  href="https://www.nationalarchives.gov.uk/enrichment/css/logo-adornments.css"
  media="screen"
/>
```

## JavaScript

Similar to the CSS entrypoint, there a single dynamic JavaScript file that will import the relevant script. Add this right at the bottom of your page, just before the closing `</body>` tag.

```html
<script
  type="module"
  src="https://www.nationalarchives.gov.uk/enrichment/js/logo-adornments.js"
  defer
></script>
```

## Cache busting

Each adornment is applied on a day-by-day basis.

The CSS is cached for an hour but a date parameter can be added to the request which changes nothing about the response but acts as a cache buster. This should be dynamically set by your service.

```
https://www.nationalarchives.gov.uk/enrichment/css/logo-adornments.css?date=2024-09-24
```

## Debug

The CSS and JavaScript can be tested by adding a `debug` parameter with a date to check the adornment for that date.

```
https://www.nationalarchives.gov.uk/enrichment/css/logo-adornments.css?debug=2025-01-01
```
