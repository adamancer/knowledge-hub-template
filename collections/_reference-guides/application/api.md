---
title: API
status: draft
parent: Application
nav_order: 2
tags: [template, api]
---

An example of an API

<h2>Pages</h2>
<ul>
{% for item in site["reference-guides"] %}
{% if item.parent == page.title %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
{% endif %}
{% endfor %}
</ul>