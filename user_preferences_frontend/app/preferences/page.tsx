"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { set } from "react-hook-form";

interface Preferences {
    account_settings: {
        id: number;
        username: string;
        email: string;
        password: string;
    };
    notification_settings: {
        id: number;
        frequency: "daily" | "weekly" | "monthly" | "on-demand";
        email_notifications: boolean;
        push_notifications: boolean;
        user: number;
    };
    theme_settings: {
        id: number;
        theme: "light" | "dark";
        font_size: "small" | "medium" | "large";
        user: number;
    };
    privacy_settings: {
        id: number;
        profile_visibility: "public" | "private";
        data_sharing: boolean;
        user: number;
    };
}


export default function Preferences() {
    const router = useRouter();
    const [preferences, setPreferences] = useState<Preferences | null>(null);
    const [theme, setTheme] = useState("light");
    const [fontSize, setFontSize] = useState("medium");

    useEffect(() => {
        const storedPreferences = sessionStorage.getItem("preferences");
        if (storedPreferences && storedPreferences !== '{"detail":"Invalid token"}') {
            setPreferences(JSON.parse(storedPreferences));
        }
        else {
            const fetchPreferences = async () => {
                const token = sessionStorage.getItem("token");
                const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/preferences/`, {
                    headers: { Authorization: `Bearer ${token}` },
                });
                const data = await res.json();
                setPreferences(data);
                setTheme(data.theme_settings.theme);
                setFontSize(data.theme_settings.font_size);
                sessionStorage.setItem("preferences", JSON.stringify(data));
            };

            fetchPreferences();
        }
    }, []);

    const handleUpdate = async (section: string, updates: any) => {
        const token = sessionStorage.getItem("token");
        const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/preferences/${section}/`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify(updates),
        });

        if (res.ok) {
            const updatedData = await res.json();
            setPreferences((prev) =>
                prev
                    ? {
                        ...prev,
                        [section]: {
                            ...(prev[section as keyof Preferences] as any),
                            ...updatedData,
                        },
                    }
                    : prev
            );
        }
        console.log("Updated", section, updates);
    };

    const handleLogout = () => {
        sessionStorage.removeItem("token");
        sessionStorage.removeItem("preferences");
        router.push("http://localhost:3000/");
    };

    if (!preferences)
        return (
            <div className="flex justify-center items-center h-screen text-xl text-gray-700 bg-gray-100 dark:text-gray-300 dark:bg-gray-900">
                Loading...
            </div>
        );

    return (
        <div
            className={`min-h-screen flex items-center justify-center p-6 ${theme === "dark" ? "bg-gray-900 text-white" : "bg-gray-100 text-gray-900"
                }`}
        >
            <div className="w-full max-w-lg bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg">
                <div className="flex justify-between items-center mb-6">
                    <h1 className="text-2xl font-bold">Preferences</h1>
                    <button
                        onClick={handleLogout}
                        className="bg-red-500 text-white py-1 px-4 rounded hover:bg-red-600 focus:outline-none"
                    >
                        Logout
                    </button>
                </div>
                <div className="space-y-6">
                    {/* Account Settings */}
                    <section>
                        <h2 className="text-lg font-semibold">Account Settings</h2>
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-200 mt-2" htmlFor="username">
                            Username
                        </label>
                        <input
                            id="username"
                            type="text"
                            defaultValue={preferences.account_settings.username}
                            onBlur={(e) =>
                                handleUpdate("account_settings", { username: e.target.value })
                            }
                            className="w-full px-3 py-2 mb-2 border rounded-md bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-200"
                        />
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-200" htmlFor="email">
                            Email
                        </label>
                        <input
                            type="email"
                            defaultValue={preferences.account_settings.email}
                            onBlur={(e) =>
                                handleUpdate("account_settings", { email: e.target.value })
                            }
                            className="w-full px-3 py-2 mb-2 border rounded-md bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-200"
                        />
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-200" htmlFor="password">
                            Password
                        </label>
                        <input
                            type="password"
                            defaultValue={preferences.account_settings.password}
                            onBlur={(e) =>
                                handleUpdate("account_settings", { password: e.target.value })
                            }
                            className="w-full px-3 py-2 border rounded-md bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-200"
                        />
                    </section>

                    {/* Notification Settings */}
                    <section>
                        <h2 className="text-lg font-semibold">Notification Settings</h2>
                        <label className="flex items-center space-x-2 mt-2">
                            <input
                                type="checkbox"
                                defaultChecked={preferences.notification_settings.email_notifications}
                                onChange={(e) =>
                                    handleUpdate("notification_settings", {
                                        email_notifications: e.target.checked,
                                    })
                                }
                                className="h-4 w-4 text-blue-600 dark:text-blue-400"
                            />
                            <span>Email Notifications</span>
                        </label>
                        <label className="flex items-center space-x-2 mt-2">
                            <input
                                type="checkbox"
                                defaultChecked={preferences.notification_settings.push_notifications}
                                onChange={(e) =>
                                    handleUpdate("notification_settings", {
                                        push_notifications: e.target.checked,
                                    })
                                }
                                className="h-4 w-4 text-blue-600 dark:text-blue-400"
                            />
                            <span>Push Notifications</span>
                        </label>
                        <label className="mt-2 block">
                            Frequency:
                            <select
                                value={preferences.notification_settings.frequency}
                                onChange={(e) =>
                                    handleUpdate("notification_settings", { frequency: e.target.value })
                                }
                                className="w-full px-3 py-2 mt-1 border rounded-md bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-200"
                            >
                                <option value="daily">Daily</option>
                                <option value="weekly">Weekly</option>
                                <option value="monthly">Monthly</option>
                                <option value="on-demand">On-Demand</option>
                            </select>
                        </label>
                    </section>

                    {/* Theme Settings */}
                    <section>
                        <h2 className="text-lg font-semibold">Theme Settings</h2>
                        <label className="block mt-2">
                            Theme:
                            <select
                                value={theme}
                                onChange={(e) => {
                                    setTheme(e.target.value);
                                    handleUpdate("theme_settings", { theme: e.target.value });
                                }}
                                className="w-full px-3 py-2 mt-1 border rounded-md bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-200"
                            >
                                <option value="light">Light</option>
                                <option value="dark">Dark</option>
                            </select>
                        </label>
                        <label className="block mt-2">
                            Font Size:
                            <select
                                value={fontSize}
                                onChange={(e) => {
                                    setFontSize(e.target.value);
                                    handleUpdate("theme_settings", { font_size: e.target.value });
                                }}
                                className="w-full px-3 py-2 mt-1 border rounded-md bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-200"
                            >
                                <option value="small">Small</option>
                                <option value="medium">Medium</option>
                                <option value="large">Large</option>
                            </select>
                        </label>
                    </section>

                    {/* Privacy Settings */}
                    <section>
                        <h2 className="text-lg font-semibold">Privacy Settings</h2>
                        <label className="block mt-2">
                            Profile Visibility:
                            <select
                                defaultValue={preferences.privacy_settings.profile_visibility}
                                onChange={(e) =>
                                    handleUpdate("privacy_settings", {
                                        profile_visibility: e.target.value,
                                    })
                                }
                                className="w-full px-3 py-2 mt-1 border rounded-md bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-200"
                            >
                                <option value="public">Public</option>
                                <option value="private">Private</option>
                            </select>
                        </label>
                        <label className="flex items-center space-x-2 mt-2">
                            <input
                                type="checkbox"
                                defaultChecked={preferences.privacy_settings.data_sharing}
                                onChange={(e) =>
                                    handleUpdate("privacy_settings", {
                                        data_sharing: e.target.checked,
                                    })
                                }
                                className="h-4 w-4 text-blue-600 dark:text-blue-400"
                            />
                            <span>Data Sharing</span>
                        </label>
                    </section>
                </div>
            </div>
        </div>
    );
}
