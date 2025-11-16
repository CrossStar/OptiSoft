function generateChartOption({ title, xData, series, legend }) {
  const totalLength = xData.length;
  const showLength = 100;
  const startPercent =
    totalLength > showLength
      ? ((totalLength - showLength) / totalLength) * 100
      : 0;

  return {
    title: { text: title, left: "center" },
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "cross",
        animation: true,
        label: { backgroundColor: "#505765" },
      },
    },
    legend: { data: legend, left: "left" },
    xAxis: {
      type: "category",
      data: xData,
      axisTick: { alignWithLabel: true },
    },
    yAxis: { type: "value" },
    dataZoom: [
      {
        show: true,
        realtime: true,
        start: 0,
        end: 100,
        xAxisIndex: [0, 1],
      },
      {
        type: "inside",
        realtime: true,
        start: 0,
        end: 100,
        xAxisIndex: [0, 1],
      },
    ],
    series,
    toolbox: {
      show: true,
      feature: {
        saveAsImage: { show: true, title: "保存为图片" },
        restore: { show: true, title: "还原" },
        dataZoom: {
          show: true,
          title: { zoom: "区域缩放", back: "区域缩放还原" },
          // yAxisIndex: "none",
        },
        mark: {
          show: true,
          title: { mark: "辅助线开关", markClear: "清空辅助线" },
        },
        dataView: {
          show: true,
          readOnly: true,
          optionToContent: function (opt) {
            var axisData = opt.xAxis[0].data; // x轴数据
            var series = opt.series;

            // 表头
            var tdHeads =
              '<td style="padding: 10px; font-weight: bold; color: #333; white-space: nowrap; min-width: 80px; max-width: 50%;">id</td>';
            series.forEach(function (item) {
              tdHeads += `<td style="padding: 10px; font-weight: bold; color: #333;">${item.name}</td>`;
            });

            // 表格样式优化
            var table = `
                <div style="overflow-x: auto; padding: 10px;">
                    <table style="width: 100%; border-collapse: collapse; font-size: 18px; text-align: center; border-radius: 8px; overflow: hidden; box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);">
                        <thead>
                            <tr style="background: #f5f5f5; border-bottom: 2px solid #ddd;">
                                ${tdHeads}
                            </tr>
                        </thead>
                        <tbody>
            `;

            // 表体
            var tdBodys = "";
            for (var i = 0, l = axisData.length; i < l; i++) {
              for (var j = 0; j < series.length; j++) {
                let cellData =
                  typeof series[j].data[i] == "object"
                    ? series[j].data[i].value
                    : series[j].data[i];
                tdBodys += `<td style="padding: 10px; color: #666;">${cellData}</td>`;
              }

              table += `
                    <tr style="border-bottom: 1px solid #ddd;">
                        <td style="padding: 10px; font-weight: bold; color: #444; white-space: nowrap; min-width: 80px; max-width: 50%; overflow: hidden; text-overflow: ellipsis;">${axisData[i]}</td>
                        ${tdBodys}
                    </tr>
                `;
              tdBodys = "";
            }

            table += `
                        </tbody>
                    </table>
                </div>
            `;
            return table;
          },
        },
      },
    },
  };
}
