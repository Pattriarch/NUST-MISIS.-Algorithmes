<div class="header">
        <h1 class="title">C. Опасный маршрут</h1>
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
            <p class="paragraph">Профессор Флойд живёт в очень опасном районе города. Ежедневно бандиты грабят на улицах прохожих. Читая криминальную хронику, профессор Флойд вычислил вероятность быть ограбленным при проходе по каждой улице города.</p>
            <p class="paragraph">Теперь он хочет найти наиболее безопасный путь от дома до университета, в котором он преподаёт. Иными словами, он хочет найти путь от дома до университета, для которого вероятность быть ограбленным минимальна.</p>
        </div>
    </div>
    <h2>Формат ввода</h2>
    <div class="input-specification">
        <div class="Markdown">
            <p class="paragraph">В первой строке находятся два числа <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>N</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">N</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span> и <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>M</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">M</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">M</span></span></span></span> - количество зданий и количество улиц, соединяющих здания (<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
                                    <mi>M</mi>
                                    <mo>≤</mo>
                                    <mfrac>
                                        <mrow>
                                            <mi>N</mi>
                                            <mo>⋅</mo>
                                            <mo stretchy="false">(</mo>
                                            <mi>N</mi>
                                            <mtext>−</mtext>
                                            <mn>1</mn>
                                            <mo stretchy="false">)</mo>
                                        </mrow>
                                        <mn>2</mn>
                                    </mfrac>
                                </mrow>
                                <annotation encoding="application/x-tex">1 \leq M \leq \frac{N \cdot (N−1)}{2}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.78041em;vertical-align:-0.13597em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8193em;vertical-align:-0.13597em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">M</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1.355em;vertical-align:-0.345em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.01em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.485em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right:0.10903em;">N</span><span class="mbin mtight">⋅</span><span class="mopen mtight">(</span><span class="mord mathnormal mtight" style="margin-right:0.10903em;">N</span><span class="mord mtight">−1</span><span class="mclose mtight">)</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>). В следующей строке находятся числа <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>S</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">S</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.05764em;">S</span></span></span></span> и <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>E</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">E</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.05764em;">E</span></span></span></span> -- номер дома, в котором живёт профессор и номер дома, в котором находится университет соответственно. Далее в <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>M</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">M</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">M</span></span></span></span> строках расположены описания дорог: 3 целых числа <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>s</mi>
                                        <mi>i</mi>
                                    </msub>
                                </mrow>
                                <annotation encoding="application/x-tex">s_i</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>e</mi>
                                        <mi>i</mi>
                                    </msub>
                                </mrow>
                                <annotation encoding="application/x-tex">e_i</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">e</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>p</mi>
                                        <mi>i</mi>
                                    </msub>
                                </mrow>
                                <annotation encoding="application/x-tex">p_i</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="mord"><span class="mord mathnormal">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span> - здания, в которых начинается и заканчивается дорога и вероятность в процентах быть ограбленным, пройдя по дороге соответственно (<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mn>1</mn>
                                    <mo>≤</mo>
                                    <msub>
                                        <mi>s</mi>
                                        <mi>i</mi>
                                    </msub>
                                    <mo separator="true">,</mo>
                                    <msub>
                                        <mi>e</mi>
                                        <mi>i</mi>
                                    </msub>
                                    <mo>≤</mo>
                                    <mi>N</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">1 \leq s_i, e_i \leq N</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.78041em;vertical-align:-0.13597em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8304100000000001em;vertical-align:-0.19444em;"></span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord mathnormal">e</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span>, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mn>0</mn>
                                    <mo>≤</mo>
                                    <msub>
                                        <mi>p</mi>
                                        <mi>i</mi>
                                    </msub>
                                    <mo>≤</mo>
                                    <mn>100</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">0 \leq p_i \leq 100</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.78041em;vertical-align:-0.13597em;"></span><span class="mord">0</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8304100000000001em;vertical-align:-0.19444em;"></span><span class="mord"><span class="mord mathnormal">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.64444em;vertical-align:0em;"></span><span class="mord">100</span></span></span></span>, дороги двунаправленные). Гарантируется, что существует хотя бы один путь от дома профессора до университета.</p>
        </div>
    </div>
    <h2>Формат вывода</h2>
    <div class="output-specification">
        <div class="Markdown">
            <p class="paragraph">Необходимо вывести одно число - минимальную возможную вероятность быть ограбленным. Выведите ответ с максимально возможной точностью.</p>
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
                        <pre>3 3
1 3
1 2 20
1 3 50
2 3 20
</pre>
                    </td>
                    <td>
                        <pre>0.36
</pre>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
