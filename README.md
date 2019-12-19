# plotly_demo



   <label> Choose the feature to plot....</label>
    <select class="form-control" id='group'>
        <option value="sepal.length">sepal.length</option>
        <option value="petal.length">petal.length</option>
        <option value="sepal.width">sepal.width</option>
        <option value="petal.width">petal.width</option>
    </select>
    
    </script>
    <div class="chart" id="bargraph">
        <script>
            var graphs = {{ plot | safe}};
            Plotly.plot('bargraph', graphs, {});
        </script>
    </div>