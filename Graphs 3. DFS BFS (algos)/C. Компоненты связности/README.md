<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Компоненты связности</h1>
      <table>
         <thead>
            <th></th>
            <th>Все языки</th>
            <th>Free pascal 2.4.4</th>
         </thead>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>5&nbsp;секунд</td>
            <td>5&nbsp;секунд</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>512Mb</td>
            <td>512Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="2">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="2">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"> Дан неориентированный невзвешенный граф. Необходимо посчитать количество его компонент связности и вывести их. </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> Во входном файле записано два числа N и M (0 &lt; N &lt;= 100000, 0 &lt;= M &lt;= 100000). В следующих M строках записаны
      по два числа i и j (1 &lt;= i, j &lt;= N), которые означают, что вершины i и j соединены ребром. 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> В первой строчке выходного файла выведите количество компонент связности. Далее выведите <!--l. 56--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> целых чисел, <!--l. 56--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>-е из них задаёт номер компоненты связности
      для <!--l. 56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>-й
      вершины. Компоненты следует нумеровать последовательными целыми числами от 1. Порядок нумерации компонент произвольный. 
   </div>
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
            <td><pre>4 2
1 2
3 4
</pre></td>
            <td><pre>2
1 1 2 2 
</pre></td>
