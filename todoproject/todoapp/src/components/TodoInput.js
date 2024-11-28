import React, { useState } from 'react';

function TodoInput({ addTask }) {
  const [task, setTask] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (task.trim()) {
      addTask(task);
      setTask('');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ margin: '20px' }}>
      <input
        type="text"
        value={task}
        onChange={(e) => setTask(e.target.value)}
        placeholder="Enter a task"
        style={{ padding: '10px', width: '200px', marginRight: '10px' }}
      />
      <button type="submit" style={{ padding: '10px 20px' }}>
        Add
      </button>
    </form>
  );
}

export default TodoInput;