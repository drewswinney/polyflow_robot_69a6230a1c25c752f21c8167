import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a627121c25c752f21c81bb",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a627121c25c752f21c81bb",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a6272b1c25c752f21c81dc","source_node_id":"69a6271e1c25c752f21c81cc","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a627151c25c752f21c81c0",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a627151c25c752f21c81c0",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a6272d1c25c752f21c81df","source_node_id":"69a6271e1c25c752f21c81cc","source_pin_id":"rear_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a627231c25c752f21c81d2",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a627231c25c752f21c81d2",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a6272e1c25c752f21c81e2","source_node_id":"69a6271e1c25c752f21c81cc","source_pin_id":"front_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a627251c25c752f21c81d7",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a627251c25c752f21c81d7",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a627301c25c752f21c81e5","source_node_id":"69a6271e1c25c752f21c81cc","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="differential_drive",
            executable="differential_drive_node",
            name="differential_drive_69a6271e1c25c752f21c81cc",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a6271e1c25c752f21c81cc",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"wheel_radius":0.05,"wheel_separation":0.3,"max_wheel_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c8e4b3f393789aad6f84:cmd_vel","name":"cmd_vel","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3c8e4b3f393789aad6f84:mode","name":"mode","direction":"input","msg_type":"polyflow_msgs/ModeState"},{"pin_id":"69a3c8e4b3f393789aad6f84:encoder_left","name":"encoder_left","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3c8e4b3f393789aad6f84:encoder_right","name":"encoder_right","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_left_motor","name":"front_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_left_motor","name":"rear_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_right_motor","name":"front_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_right_motor","name":"rear_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:odometry","name":"odometry","direction":"output","msg_type":"nav_msgs/Odometry"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a627391c25c752f21c81ef","source_node_id":"69a6271b1c25c752f21c81c6","source_pin_id":"encoder_state","target_pin_id":"encoder_left"},{"connection_id":"69a6273b1c25c752f21c81f2","source_node_id":"69a627351c25c752f21c81eb","source_pin_id":"encoder_state","target_pin_id":"encoder_right"},{"connection_id":"69a627481c25c752f21c8206","source_node_id":"69a627441c25c752f21c8202","source_pin_id":"mode","target_pin_id":"mode"},{"connection_id":"69a627501c25c752f21c8210","source_node_id":"69a6274d1c25c752f21c820c","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"},{"connection_id":"69a627521c25c752f21c8213","source_node_id":"69a6273e1c25c752f21c81f7","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a6272b1c25c752f21c81dc","target_node_id":"69a627121c25c752f21c81bb","source_pin_id":"front_left_motor","target_pin_id":"command"},{"connection_id":"69a6272d1c25c752f21c81df","target_node_id":"69a627151c25c752f21c81c0","source_pin_id":"rear_left_motor","target_pin_id":"command"},{"connection_id":"69a6272e1c25c752f21c81e2","target_node_id":"69a627231c25c752f21c81d2","source_pin_id":"front_right_motor","target_pin_id":"command"},{"connection_id":"69a627301c25c752f21c81e5","target_node_id":"69a627251c25c752f21c81d7","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_69a6271b1c25c752f21c81c6",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a6271b1c25c752f21c81c6",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c932b3f393789aad6fbc:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3c932b3f393789aad6fbc:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a627391c25c752f21c81ef","target_node_id":"69a6271e1c25c752f21c81cc","source_pin_id":"encoder_state","target_pin_id":"encoder_left"}]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_69a627351c25c752f21c81eb",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a627351c25c752f21c81eb",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c932b3f393789aad6fbc:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3c932b3f393789aad6fbc:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a6273b1c25c752f21c81f2","target_node_id":"69a6271e1c25c752f21c81cc","source_pin_id":"encoder_state","target_pin_id":"encoder_right"}]')),
            }
        ),
        Node(
            package="logger",
            executable="logger_node",
            name="logger_69a627421c25c752f21c81fd",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a627421c25c752f21c81fd",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"log_file":"","log_to_stdout":true}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="mode_switcher",
            executable="mode_switcher_node",
            name="mode_switcher_69a627441c25c752f21c8202",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a627441c25c752f21c8202",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"default_mode":"stopped","allowed_modes":["teleop","automated","stopped"]}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd36b3f393789aad7079:set_mode","name":"set_mode","direction":"input","msg_type":"polyflow_msgs/ModeCommand"},{"pin_id":"69a3cd36b3f393789aad7079:mode","name":"mode","direction":"output","msg_type":"polyflow_msgs/ModeState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a627481c25c752f21c8206","target_node_id":"69a6271e1c25c752f21c81cc","source_pin_id":"mode","target_pin_id":"mode"}]')),
            }
        ),
        Node(
            package="mission_runner",
            executable="mission_runner_node",
            name="mission_runner_69a6273e1c25c752f21c81f7",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a6273e1c25c752f21c81f7",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"mission":[],"linear_speed":0.5,"angular_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":10,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a477bcc85549d8e55e27db:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a477bcc85549d8e55e27db:status","name":"status","direction":"output","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a627521c25c752f21c8213","target_node_id":"69a6271e1c25c752f21c81cc","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="gamepad",
            executable="gamepad_node",
            name="gamepad_69a6274d1c25c752f21c820c",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a6274d1c25c752f21c820c",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"device_index":0,"poll_rate_hz":60,"deadzone":0.05,"max_linear_speed":1,"max_angular_speed":2}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":60,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c77bb3f393789aad6f62:axes","name":"axes","direction":"output","msg_type":"polyflow_msgs/GamepadAxes"},{"pin_id":"69a3c77bb3f393789aad6f62:buttons","name":"buttons","direction":"output","msg_type":"polyflow_msgs/GamepadButtons"},{"pin_id":"69a3c77bb3f393789aad6f62:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a627501c25c752f21c8210","target_node_id":"69a6271e1c25c752f21c81cc","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
    ])