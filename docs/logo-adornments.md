# Logo adornments

Adornments can be added to logos in both the [header](https://nationalarchives.github.io/design-system/components/header/) and [global header](https://nationalarchives.github.io/design-system/components/global-header/) components.

There is a single entry file ([/enrichment/css/logo-adornments.css](http://localhost:65529/enrichment/css/logo-adornments.css)) that dynamically imports the relevant adornment based on the current date.

These adornments can be included on any service that uses the components from TNA Frontend by including the CSS in the header:

```html
<link
  rel="stylesheet"
  href="https://tna.dblclk.dev/enrichment/css/logo-adornments.css"
  media="screen"
  crossorigin="anonymous"
/>
```

A date parameter can be added which changes nothing about the output but acts as a cache buster as each adornment is applied on a day-by-day basis. This should be dynamically set by your service.

```
https://tna.dblclk.dev/enrichment/css/logo-adornments.css?date=2024-09-24
```
