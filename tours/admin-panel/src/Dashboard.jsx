// src/Dashboard.jsx
import React, { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { auth } from './firebase'

function Dashboard() {
  const navigate = useNavigate()
  const user = auth.currentUser

  useEffect(() => {
    if (!user) {
      navigate('/')
    }
  }, [user, navigate])

  return (
    <div className="h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-6 rounded shadow-md">
        <h1 className="text-xl font-bold mb-2">🎉 登入成功</h1>
        <p>歡迎 {user?.displayName || user?.email}！</p>
      </div>
    </div>
  )
}

export default Dashboard