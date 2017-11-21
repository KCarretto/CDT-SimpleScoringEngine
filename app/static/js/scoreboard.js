
function build_scoreboard() {
    var oldscoreboard = document.getElementById("scoreboard");
    var scoreboard = oldscoreboard.cloneNode(true);

    // Clear scoreboard
    while (scoreboard.hasChildNodes()) {
        scoreboard.removeChild(scoreboard.lastChild);
    }

    // Rebuild scoreboard
    tablehead = document.createElement("thead");
    scoreboard.appendChild(tablehead);
    tableheadrow = document.createElement("tr");
    tablehead.appendChild(tableheadrow);
    tablestatusrow = document.createElement("tr");
    scoreboard.appendChild(tablestatusrow);

    // Fetch new scoreboard data
    var scoredata;
    $.getJSON("/api/round", 
        function(json) {
            // Fill in table with statuses
            for (i in json.checks) {
                header = document.createElement("th");
                header.innerText = json.checks[i].check_type;
                tableheadrow.appendChild(header);

                statusNode = document.createElement("td");
                statusNode.innerText = json.checks[i].check_status;
                tablestatusrow.appendChild(statusNode);
            }

            oldscoreboard.parentNode.replaceChild(scoreboard, oldscoreboard);
        }
    );
}

$( document ).ready(
    function() {
        build_scoreboard();
        setInterval(build_scoreboard, 1000);
    }
);

/*
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
*/