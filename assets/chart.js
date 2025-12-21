// docs/javascripts/charts.js
document$.subscribe(function() {
  const canvas = document.getElementById('myChart');
  if (canvas) {
    new Chart(canvas, {
      type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: { beginAtZero: true }
      }
    }
    });
  }
});
