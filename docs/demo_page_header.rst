{% for _builder in ["html", "ubtrace"] %}
.. if-builder:: {{ _builder }}

   .. dropdown:: Demo page details
      :icon: light-bulb
      :color: success

      **Page source code: {{page}}**

      .. literalinclude:: {{page}}
         :language: rst
         :linenos:
{% endfor %}
