export default function createPushNotificationsJobs(jobs, queue) {
	if (!Array.isArray(jobs)) throw new Error('Jobs is not an array')

	jobs.forEach((obj) => {
		const newJob = queue.create('push_notification_code_3', obj).save()
		newJob
			.on('enqueue', () => console.log(`Notification job created: ${newJob.id}`))
			.on('complete', () => console.log(`Notification job ${newJob.id} completed`))
			.on('failed', (errorMessage) => console.log(`Notification job ${newJob.id} failed: ${errorMessage}`))
			.on('progress', (progress, data) => console.log(`Notification job ${newJob.id} ${progress}% complete`))
	})
}
