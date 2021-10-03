<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. DM Algos. От матрицы смежности к списку ребер, ориентированный вариант</h1>
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
         <p>Ориентированный граф задан матрицей смежности, выведите его представление в виде списка ребер.</p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>На вход программы поступает число n (1&lt;=n&lt;=100) – количество вершин графа, а затем n строк по n чисел, каждое из которых равно
            0 или 1, – его матрица смежности.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите список ребер заданного графа.</p></span></div>
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
            <td><pre>5
0 0 0 0 0 
0 0 0 0 1 
1 1 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
</pre></td>
            <td><pre>2 5
3 1
3 2
</pre></td>
