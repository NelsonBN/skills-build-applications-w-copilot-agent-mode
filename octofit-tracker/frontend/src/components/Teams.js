import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://automatic-lamp-4v5vqr9v92jq55-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Teams</h1>
        <ul className="list-group">
          {teams.map(team => (
            <li key={team._id} className="list-group-item">{team.name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Teams;
