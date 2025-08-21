import React, { useState } from "react"; import { Card, CardContent } from "@/components/ui/card"; import { Button } from "@/components/ui/button"; import { Input } from "@/components/ui/input"; import { motion } from "framer-motion";

// 운동 및 스트레칭 데이터 const workoutData = [ { name: "푸쉬업", type: "운동", url: "https://www.youtube.com/embed/IODxDxX7oi4" }, { name: "스쿼트", type: "운동", url: "https://www.youtube.com/embed/aclHkVaku9U" }, { name: "플랭크", type: "운동", url: "https://www.youtube.com/embed/pSHjTRCQxIw" }, { name: "런지", type: "운동", url: "https://www.youtube.com/embed/QOVaHwm-Q6U" }, { name: "햄스트링 스트레칭", type: "스트레칭", url: "https://www.youtube.com/embed/yR5Vm1nR1UQ" }, { name: "어깨 스트레칭", type: "스트레칭", url: "https://www.youtube.com/embed/eX2qFMC8cFo" }, { name: "고양이 소 스트레칭", type: "스트레칭", url: "https://www.youtube.com/embed/kqnua4rHVVA" }, { name: "허리 스트레칭", type: "스트레칭", url: "https://www.youtube.com/embed/gQdf8cpDZ38" }, ];

export default function WorkoutApp() { const [search, setSearch] = useState("");

// 검색 필터링 const filteredWorkouts = workoutData.filter((w) => w.name.toLowerCase().includes(search.toLowerCase()) );

return ( <div className="min-h-screen bg-gray-100 p-6"> <motion.h1 className="text-3xl font-bold text-center mb-6" initial={{ opacity: 0, y: -20 }} animate={{ opacity: 1, y: 0 }} > 운동 & 스트레칭 루틴 </motion.h1>

{/* 검색창 */}
  <div className="flex justify-center mb-6">
    <Input
      placeholder="운동이나 스트레칭 검색..."
      value={search}
      onChange={(e) => setSearch(e.target.value)}
      className="w-1/2 shadow-md"
    />
  </div>

  {/* 운동 목록 */}
  <h2 className="text-xl font-semibold mb-3">운동</h2>
  <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-10">
    {filteredWorkouts
      .filter((w) => w.type === "운동")
      .map((workout, index) => (
        <Card key={index} className="shadow-lg rounded-2xl overflow-hidden">
          <CardContent>
            <h3 className="text-lg font-semibold mb-2">{workout.name}</h3>
            <iframe
              className="w-full h-56 rounded-lg"
              src={`${workout.url}?rel=0&autoplay=0`}
              title={workout.name}
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            ></iframe>
          </CardContent>
        </Card>
      ))}
  </div>

  {/* 스트레칭 목록 */}
  <h2 className="text-xl font-semibold mb-3">스트레칭</h2>
  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
    {filteredWorkouts
      .filter((w) => w.type === "스트레칭")
      .map((stretch, index) => (
        <Card key={index} className="shadow-lg rounded-2xl overflow-hidden">
          <CardContent>
            <h3 className="text-lg font-semibold mb-2">{stretch.name}</h3>
            <iframe
              className="w-full h-56 rounded-lg"
              src={`${stretch.url}?rel=0&autoplay=0`}
              title={stretch.name}
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            ></iframe>
          </CardContent>
        </Card>
      ))}
  </div>
</div>

); }

