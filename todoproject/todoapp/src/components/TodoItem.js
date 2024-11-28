import React from 'react';

function TodoItem({ task, toggleTaskCompletion }) {
  return (
    <div
      style={{
        margin: '10px',
        padding: '10px',
        border: '1px solid #ddd',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
      }}
    >
      <span
        style={{
          textDecoration: task.isCompleted ? 'line-through' : 'none',
          color: task.isCompleted ? '#aaa' : '#000',
        }}
      >
        {task.text}
      </span>
      <input
        type="checkbox"
        checked={task.isCompleted}
        onChange={toggleTaskCompletion}
        style={{ cursor: 'pointer' }}
      />
    </div>
  );
}

export default TodoItem;
