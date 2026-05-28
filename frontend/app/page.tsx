'use client'

import { useEffect, useState } from 'react'

export default function Home() {
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL
    
    if (!apiUrl) {
      console.error("API URL is not defined in environment variables")
      return
    }

    fetch(`${apiUrl}/tasks`)
      .then(res => res.json())
      .then(data => setTasks(data))
      .catch(err => console.error("Failed to fetch tasks:", err))
  }, [])

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold">Task Manager</h1>

      {tasks.map((task: any, index: number) => (
        <div key={index}>{task.title}</div>
      ))}
    </div>
  )
}