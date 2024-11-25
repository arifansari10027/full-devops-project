import React from 'react';
import TodoItem from './TodoItem';

function TodoList({ tasks, toggleTaskCompletion }) {
  return (
    <div>
      {tasks.length === 0 ? (
        <p>No tasks added yet.</p>
      ) : (
        tasks.map((task, index) => (
          <TodoItem
            key={index}
            task={task}
            toggleTaskCompletion={() => toggleTaskCompletion(index)}
          />
        ))
      )}
    </div>
  );
}

export default TodoList;
