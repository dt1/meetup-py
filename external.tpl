<h1>{{ttl}}</h1>

{{na_list}}

<ul>
  % for i in na_list:
  <li>{{i[0]}} -- {{i[1]}}</li>
  % end
</ul>

<ul>
  % for i in na_list:
  % if i[1]:
  <li>{{i[0]}} -- {{i[1]}}</li>
  % else:
  <li>{{i[0]}} -- don't know</li>
  % end
  % end
</ul>

<ul>
  % for i in na_list:
  <li>{{i[0]}} -- {{i[1] if i[1] else "don't know"}}</li>
  % end
</ul>
