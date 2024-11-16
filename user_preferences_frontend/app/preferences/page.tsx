"use client";

import { useState, useEffect } from "react";

interface Preferences {
    username: string;
    email: string;
    password: string;
    notification_settings: {
        email_notifications: boolean;
        push_notifications: boolean;
        frequency: "daily" | "weekly" | "monthly" | "on-demand";
    };
    theme_settings: {
        theme: "light" | "dark";
        font_size: "small" | "medium" | "large";
    };
    privacy_settings: {
        profile_visibility: "public" | "private";
        data_sharing: boolean;
    };
}

export default function Preferences() {
    const [preferences , setPreferences] = useState<Preferences | null>(null);
    const [theme, setTheme] = useState("light");
    const [fontSize, setFontSize] = useState("medium");

    useEffect(() => {
        const fetchPreferences = async () => {
            const token = localStorage.getItem("token");
            const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/preferences/`, {
                headers: { Authorization: `Bearer ${token}` },
            });
            const data = await res.json();
            setPreferences(data);
            setTheme(data.theme_settings.theme);
            setFontSize(data.theme_settings.font_size);
        };

        fetchPreferences();
    }, []);

    const handleUpdate = async (section: string, updates: any) => {
        const token = localStorage.getItem("token");
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
            setPreferences((prev) => prev ? ({ ...prev, [section]: { ...(prev[section as keyof Preferences] as any), ...updatedData } }) : prev);
        }
    };

    if (!preferences) return (
        <div className="flex justify-center items-center h-screen text-xl text-gray-700 bg-gray-100 dark:text-gray-300 dark:bg-gray-900">
            Loading...
        </div>
    );
    else {
        return (
            <div
                className={`min-h-screen p-6 ${theme === "dark" ? "bg-gray-900 text-white" : "bg-white text-gray-900"
                    }`}
            >
                <h1 className="text-2xl font-bold mb-6">Preferences</h1>
                <div className="space-y-6">
                    {/* Account Settings */}
                    <section>
                        <h2 className="text-xl font-semibold">Account Settings</h2>
                        <input
                            type="text"
                            defaultValue={preferences.username}
                            onBlur={(e) =>
                                handleUpdate("account_settings", { username: e.target.value })
                            }
                            className="w-full px-3 py-2 border rounded-md"
                        />
                        <input
                            type="email"
                            defaultValue={preferences.email}
                            onBlur={(e) =>
                                handleUpdate("account_settings", { email: e.target.value })
                            }
                            className="w-full px-3 py-2 border rounded-md mt-2"
                        />
                        {/* input field to change password with best practices */}
                        <input
                            type="password"
                            defaultValue={preferences.password}
                            onBlur={(e) =>
                                handleUpdate("account_settings", { password: e.target.value })
                            }
                            className="w-full px-3 py-2 border rounded-md mt-2"
                        />
                    </section>

                    {/* Notification Settings */}
                    <section>
                        <h2 className="text-xl font-semibold">Notification Settings</h2>
                        <label>
                            <input
                                type="checkbox"
                                defaultChecked={preferences.notification_settings.email_notifications}
                                onChange={(e) =>
                                    handleUpdate("notification_settings", {
                                        email_notifications: e.target.checked,
                                    })
                                }
                            />{" "}
                            Email Notifications
                        </label>
                        <label>
                            <input
                                type="checkbox"
                                defaultChecked={preferences.notification_settings.push_notifications}
                                onChange={(e) =>
                                    handleUpdate("notification_settings", {
                                        push_notifications: e.target.checked,
                                    })
                                }
                            />{" "}
                            Push Notifications
                        </label>
                        <label>
                            Frequency:
                            <select
                                value={preferences.notification_settings.frequency}
                                onChange={(e) => handleUpdate("notification_settings", { frequency: e.target.value })}
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
                        <h2 className="text-xl font-semibold">Theme Settings</h2>
                        <select
                            value={theme}
                            onChange={(e) => {
                                setTheme(e.target.value);
                                handleUpdate("theme_settings", { theme: e.target.value });
                            }}
                            className="w-full px-3 py-2 border rounded-md"
                        >
                            <option value="light">Light</option>
                            <option value="dark">Dark</option>
                        </select>

                        <label>
                            Font Size:
                            <select
                                value={fontSize}
                                onChange={(e) => {
                                    setFontSize(e.target.value);
                                    handleUpdate("theme_settings", { font_size: e.target.value });
                                }}
                            >
                                <option value="small">Small</option>
                                <option value="medium">Medium</option>
                                <option value="large">Large</option>
                            </select>
                        </label>
                    </section>

                    {/* Privacy Settings */}
                    <section>
                        <h2 className="text-xl font-semibold">Privacy Settings</h2>
                        <select
                            defaultValue={preferences.privacy_settings.profile_visibility}
                            onChange={(e) =>
                                handleUpdate("privacy_settings", {
                                    profile_visibility: e.target.value,
                                })
                            }
                            className="w-full px-3 py-2 border rounded-md"
                        >
                            <option value="public">Public</option>
                            <option value="private">Private</option>
                        </select>

                        <label>
                            <input
                                type="checkbox"
                                defaultChecked={preferences.privacy_settings.data_sharing}
                                onChange={(e) =>
                                    handleUpdate("privacy_settings", {
                                        allow_dms: e.target.checked,
                                    })
                                }
                            />{" "}
                            Data Sharing
                        </label>
                    </section>
                </div>
            </div>
        );
    }
}
