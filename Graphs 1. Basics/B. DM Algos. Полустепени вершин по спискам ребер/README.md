<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. DM Algos. Полустепени вершин по спискам ребер</h1>
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
         <p>Ориентированный граф задан списком ребер. Найдите степени всех вершин графа.</p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала вводятся числа n (1 &lt;= n &lt;= 100) – количество вершин в графе и m (1 &lt;= m &lt;= n(n-1)) – количество ребер. Затем следует
            m пар чисел – ребра графа.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите n пар чисел – для каждой вершины сначала выведите полустепень захода и затем полустепень исхода.</p></span></div>
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
            <td><pre>5 3
2 5
3 1
3 2
</pre></td>
            <td><pre>1
0
1
1
0
2
0
0
1
0
</pre></td>
