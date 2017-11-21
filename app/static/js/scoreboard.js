
function build_scoreboard() {
    var scoreboard = document.getElementById("scoreboard");
    
    // Clear scoreboard
    while (scoreboard.firstChild) {
        scoreboard.removeChild(scoreboard.firstChild);
    }

    scoretable = document.createElement("table");
    scoreboard.appendChild(scoretable);

    tablehead = document.createElement("thead");
    scoretable.appendChild(tablehead);

    // Fetch new scoreboard data
    var scoredata;
    $.getJSON("/api/round", function(json){
        scoredataa = json;
    });

    var oldTable = document.getElementById('scoretable'),
    newTable = oldTable.cloneNode(true);
    
    for(var i = 0; i < json_example.length; i++){
        var tr = document.createElement('tr');
        for(var j = 0; j < json_example[i].length; j++){
            var td = document.createElement('td');
            td.appendChild(document.createTextNode(json_example[i][j]));
            tr.appendChild(td);
        }
        newTable.appendChild(tr);
    }

    oldTable.parentNode.replaceChild(newTable, oldTable);
}

$( document ).ready(
    function() {
        setInterval(build_scoreboard, 3000);
    }
);

<table>
        <thead>
          <tr>
              <th>Name</th>
              <th>Item Name</th>
              <th>Item Price</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td>Alvin</td>
            <td>Eclair</td>
            <td>$0.87</td>
          </tr>
          <tr>
            <td>Alan</td>
            <td>Jellybean</td>
            <td>$3.76</td>
          </tr>
          <tr>
            <td>Jonathan</td>
            <td>Lollipop</td>
            <td>$7.00</td>
          </tr>
        </tbody>
      </table>