"use client";

import { useState } from "react";
import { AiFillEye, AiFillEyeInvisible } from "react-icons/ai";

export default function RegisterPage() {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        if (password !== confirmPassword) {
            alert("Passwords do not match");
            return;
        }

        try {
            const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/register/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, email, password }),
            });

            if (!res.ok) {
                const { detail } = await res.json();
                throw new Error(detail || "Registration failed");
            }

            const data = await res.json();
            sessionStorage.setItem("token", data.token);
            window.location.href = "/preferences";
        } catch (error) {
            if (error instanceof Error) {
                alert(error.message);
            } else {
                alert("An unknown error occurred");
            }
        }
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
            <form onSubmit={handleSubmit} className="bg-white p-8 shadow-md rounded-lg w-96 space-y-6">
                <h1 className="text-2xl font-bold text-center">Register</h1>
                <div>
                    <label className="block text-sm font-medium text-gray-700">Username</label>
                    <input
                        type="text"
                        required
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        className="w-full px-3 py-2 border rounded-md focus:ring focus:ring-blue-300"
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700">Email</label>
                    <input
                        type="email"
                        required
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="w-full px-3 py-2 border rounded-md focus:ring focus:ring-blue-300"
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700">Password</label>
                    <div className="relative">
                        <input
                            type={showPassword ? "text" : "password"}
                            required
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full px-3 py-2 border rounded-md focus:ring focus:ring-blue-300"
                        />
                        <button
                            type="button"
                            onClick={() => setShowPassword(!showPassword)}
                            className="absolute inset-y-0 right-0 px-3 flex items-center focus:outline-none"
                        >
                            {showPassword ? (
                                <AiFillEyeInvisible className="h-5 w-5 text-gray-500" />
                            ) : (
                                <AiFillEye className="h-5 w-5 text-gray-500" />
                            )}
                        </button>
                    </div>
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700">Confirm Password</label>
                    <div className="relative">
                        <input
                            type={showConfirmPassword ? "text" : "password"}
                            required
                            value={confirmPassword}
                            onChange={(e) => setConfirmPassword(e.target.value)}
                            className="w-full px-3 py-2 border rounded-md focus:ring focus:ring-blue-300"
                        />
                        <button
                            type="button"
                            onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                            className="absolute inset-y-0 right-0 px-3 flex items-center focus:outline-none"
                        >
                            {showConfirmPassword ? (
                                <AiFillEyeInvisible className="h-5 w-5 text-gray-500" />
                            ) : (
                                <AiFillEye className="h-5 w-5 text-gray-500" />
                            )}
                        </button>
                    </div>
                </div>
                <button type="submit" className="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 focus:outline-none">
                    Register
                </button>
                <p className="text-center text-sm text-gray-600">
                    Already have an account? <a href="/" className="text-blue-500 hover:underline">Login</a>
                </p>
            </form>
        </div>
    );
}