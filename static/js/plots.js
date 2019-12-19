$('#group').on('change',function(){

    $.ajax({
        url: "/change",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'selected': document.getElementById('group').value,
        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('bargraph', data );
        }
    });
})