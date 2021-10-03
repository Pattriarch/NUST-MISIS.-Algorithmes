<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. DM Algos. Полный граф</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>5&nbsp;секунд</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>640Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Неориентированный граф с кратными рёбрами называется полным, если любая пара его различных вершин соединена хотя бы одним
            ребром. Для заданного списком ребер графа проверьте, является ли он полным.
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала вводятся числа n (1 &lt;= n &lt;= 100) – количество вершин в графе и m (1 &lt;= m &lt;=10000) – количество ребер. Затем следует
            m пар чисел – ребра графа.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите «YES», если граф является полным, и «NO» в противном случае.</p></span></div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>5 18
1 2
1 3
1 3
1 4
1 4
1 4
1 5
1 5
2 3
2 4
2 4
2 5
3 4
3 4
3 4
3 5
3 5
4 5
</pre></td>
            <td><pre>YES
</pre></td>
