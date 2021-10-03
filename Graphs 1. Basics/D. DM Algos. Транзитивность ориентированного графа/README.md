<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. DM Algos. Транзитивность ориентированного графа</h1>
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
         <p>Напомним, что ориентированный граф называется транзитивным, если для любых трех различных вершин u, v и w из того, что из
            u в вершину v ведет ребро и из вершины v в вершину w ведет ребро, следует, что из вершины u в вершину w ведет ребро. Проверьте,
            что заданный ориентированный граф является транзитивным.
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала вводится число n (1&lt;=n&lt;=100) – количество вершин в графе, а затем n строк по n чисел, каждое из которых равно 0 или
            1, – его матрица смежности.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите «YES», если граф является транзитивным, и «NO» в противном случае.</p></span></div>
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
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
</pre></td>
            <td><pre>YES
</pre></td>
