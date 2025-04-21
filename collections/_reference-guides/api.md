---
title: API
status: draft
tags: [template, api]
---

A landing page for an API reference guide

<h2>Pages</h2>
<ul>
{% for item in site["reference-guides"] %}
{% if item.parent == "API" %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
{% endif %}
{% endfor %}
</ul>
