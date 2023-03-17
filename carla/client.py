from environment import CarlaEnv
from recorder import Recorder

def main():
    try:
        host = '192.168.0.114'
        port = 2000
        img_width = 640
        img_height = 640
        n_frames = 500
        fps = 30
        filename = 'intersection_15_vehicles'

        env = CarlaEnv(host, port, img_width, img_height, n_frames, fps)
        recorder = Recorder(img_width, img_height, filename)

        env.set_sync_mode()

        env.add_intersection(-47, 21)

        env.spawn_pedestrians(spawn_point_indices=[1, 71, 48, 181, 172, 188, 24, 9, 81, 14])
        env.move_pedestrians()

        vehicle_1 = env.spawn_vehicle('vehicle.tesla.model3', 79)
        vehicle_2 = env.spawn_vehicle('vehicle.audi.tt', 137)
        vehicle_3 = env.spawn_vehicle('vehicle.audi.a2', 51)
        vehicle_4 = env.spawn_vehicle('vehicle.nissan.micra', 52)
        vehicle_5 = env.spawn_vehicle('vehicle.audi.etron', 102)
        vehicle_6 = env.spawn_vehicle('vehicle.citroen.c3', 99)
        vehicle_7 = env.spawn_vehicle('vehicle.ford.mustang', 91)
        vehicle_8 = env.spawn_vehicle('vehicle.ford.crown', 1)
        vehicle_9 = env.spawn_vehicle('vehicle.mercedes.coupe', 138)
        vehicle_10 = env.spawn_vehicle('vehicle.mini.cooper_s', 35)
        vehicle_11 = env.spawn_vehicle('vehicle.nissan.patrol', 28)
        vehicle_12 = env.spawn_vehicle('vehicle.audi.a2', 27)
        vehicle_13 = env.spawn_vehicle('vehicle.tesla.model3', 49)
        vehicle_14 = env.spawn_vehicle('vehicle.mercedes.coupe', 50)
        vehicle_15 = env.spawn_vehicle('vehicle.tesla.model3', 101)

        camera_1 = env.spawn_camera((0, 0, 2), vehicle=vehicle_1)
        camera_2 = env.spawn_camera((0, 0, 2), vehicle=vehicle_2)
        camera_3 = env.spawn_camera((0, 0, 2), vehicle=vehicle_3)
        camera_4 = env.spawn_camera((0, 0, 2), vehicle=vehicle_4)
        camera_5 = env.spawn_camera((0, 0, 2), vehicle=vehicle_5)
        camera_6 = env.spawn_camera((0, 0, 2), vehicle=vehicle_6)
        camera_7 = env.spawn_camera((0, 0, 2), vehicle=vehicle_7)
        camera_8 = env.spawn_camera((0, 0, 2), vehicle=vehicle_8)
        camera_9 = env.spawn_camera((0, 0, 2), vehicle=vehicle_9)
        camera_10 = env.spawn_camera((0, 0, 2), vehicle=vehicle_10)
        camera_11 = env.spawn_camera((0, 0, 2), vehicle=vehicle_11)
        camera_12 = env.spawn_camera((0, 0, 2), vehicle=vehicle_12)
        camera_13 = env.spawn_camera((0, 0, 2), vehicle=vehicle_13)
        camera_14 = env.spawn_camera((0, 0, 2), vehicle=vehicle_14)
        camera_15 = env.spawn_camera((0, 0, 2), vehicle=vehicle_15)
        camera_16 = env.spawn_camera((-62, 3, 20), (-37, 45, 0))

        camera_1.listen(lambda image: recorder.sensor_callback(image, 'camera_1'))
        camera_2.listen(lambda image: recorder.sensor_callback(image, 'camera_2'))
        camera_3.listen(lambda image: recorder.sensor_callback(image, 'camera_3'))
        camera_4.listen(lambda image: recorder.sensor_callback(image, 'camera_4'))
        camera_5.listen(lambda image: recorder.sensor_callback(image, 'camera_5'))
        camera_6.listen(lambda image: recorder.sensor_callback(image, 'camera_6'))
        camera_7.listen(lambda image: recorder.sensor_callback(image, 'camera_7'))
        camera_8.listen(lambda image: recorder.sensor_callback(image, 'camera_8'))
        camera_9.listen(lambda image: recorder.sensor_callback(image, 'camera_9'))
        camera_10.listen(lambda image: recorder.sensor_callback(image, 'camera_10'))
        camera_11.listen(lambda image: recorder.sensor_callback(image, 'camera_11'))
        camera_12.listen(lambda image: recorder.sensor_callback(image, 'camera_12'))
        camera_13.listen(lambda image: recorder.sensor_callback(image, 'camera_13'))
        camera_14.listen(lambda image: recorder.sensor_callback(image, 'camera_14'))
        camera_15.listen(lambda image: recorder.sensor_callback(image, 'camera_15'))
        camera_16.listen(lambda image: recorder.sensor_callback(image, 'camera_16'))

        env.set_autopilot()

        curr_frame = 0

        while curr_frame < n_frames:
            env.world.tick()
            recorder.process_transforms(env.vehicle_list, env.transforms)
            recorder.process_velocities(env.vehicle_list, env.velocities)
            recorder.process_images(env.sensor_list, env.images)
            curr_frame += 1

    except KeyboardInterrupt:
        print('\nCancelled by user')
    finally:
        metadata_json = env.create_metadata()
        env.set_original_settings()
        env.clear_actors()
        recorder.create_datasets(env.transforms, env.velocities, env.images, env.vehicle_list,
                                 env.sensor_list, metadata_json)
        recorder.stop_recording()

if __name__ == '__main__':
    main()
