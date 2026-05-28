'use client'

import { useEffect, useState } from 'react'

export default function Home() {
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    fetch('http://localhost:8000/tasks')
      .then(res => res.json())
      .then(data => setTasks(data))
  }, [])

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold">Task Manager</h1>

      {tasks.map((task: any, index) => (
        <div key={index}>{task.title}</div>
      ))}
    </div>
  )
}