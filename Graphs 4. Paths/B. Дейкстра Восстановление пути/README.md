  <div class="header">
        <h1 class="title">B. Дейкстра: восстановление пути</h1>
        <table class="limits">
            <tbody>
                <tr class="time-limit">
                    <td class="property-title">Ограничение времени</td>
                    <td>1 секунда</td>
                </tr>
                <tr class="memory-limit">
                    <td class="property-title">Ограничение памяти</td>
                    <td>64.0 Мб</td>
                </tr>
                <tr class="input-file">
                    <td class="property-title">Ввод</td>
                    <td colSpan="1">стандартный ввод или input.txt</td>
                </tr>
                <tr class="output-file">
                    <td class="property-title">Вывод</td>
                    <td colSpan="1">стандартный вывод или output.txt</td>
                </tr>
            </tbody>
        </table>
    </div>
    <h2></h2>
    <div class="legend">
        <div class="Markdown">
            <p class="paragraph">Дан ориентированный взвешенный граф. Найдите кратчайший путь от одной заданной вершины до другой.</p>
        </div>
    </div>
    <h2>Формат ввода</h2>
    <div class="input-specification">
        <div class="Markdown">
            <p class="paragraph">В первой строке содержатся три числа: <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>N</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">N</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span>, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>S</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">S</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.05764em;">S</span></span></span></span> и <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>F</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">F</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.13889em;">F</span></span></span></span> (<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mn>1</mn>
                                    <mo>≤</mo>
                                    <mi>N</mi>
                                    <mo>≤</mo>
                                    <mn>100</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">1 \leq N \leq 100</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.78041em;vertical-align:-0.13597em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8193em;vertical-align:-0.13597em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.64444em;vertical-align:0em;"></span><span class="mord">100</span></span></span></span>, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mn>1</mn>
                                    <mo>≤</mo>
                                    <mi>S</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">1 \leq S</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.78041em;vertical-align:-0.13597em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.05764em;">S</span></span></span></span>, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>F</mi>
                                    <mo>≤</mo>
                                    <mi>N</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">F \leq N</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8193em;vertical-align:-0.13597em;"></span><span class="mord mathnormal" style="margin-right:0.13889em;">F</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span>), где <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>N</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">N</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span> – количество вершин графа, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>S</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">S</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.05764em;">S</span></span></span></span> – начальная вершина, а <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>F</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">F</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.13889em;">F</span></span></span></span> – конечная. В следующих <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>N</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">N</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span> строках вводится по <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>N</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">N</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span> чисел, не превосходящих <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mn>100</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">100</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.64444em;vertical-align:0em;"></span><span class="mord">100</span></span></span></span>, – матрица смежности графа, где <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mo>−</mo>
                                    <mn>1</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">-1</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.72777em;vertical-align:-0.08333em;"></span><span class="mord">−</span><span class="mord">1</span></span></span></span> означает отсутствие ребра между вершинами, а любое неотрицательное число – присутствие ребра данного веса. На главной диагонали матрицы записаны нули.</p>
        </div>
    </div>
    <h2>Формат вывода</h2>
    <div class="output-specification">
        <div class="Markdown">
            <p class="paragraph">Требуется вывести последовательно все вершины одного (любого) из кратчайших путей, или одно число -1, если пути между указанными вершинами не существует.</p>
        </div>
    </div>
    <h2>Пример</h2>
    <div>
        <table class="sample-tests">
            <thead>
                <tr>
                    <th>Ввод</th>
                    <th>Вывод</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>
                        <pre>3 2 1
0 1 1
4 0 1
2 1 0
</pre>
                    </td>
                    <td>
                        <pre>2 3 1</pre>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
