
using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class PointStampedSubscriber : Subscriber<Messages.Geometry.PointStamped>
    {
        public Transform PublishedTransform;

        private Vector3 position;
        private bool isMessageReceived;

        protected override void Start()
        {
            base.Start();
        }

        private void Update()
        {
            if (isMessageReceived)
                ProcessMessage();
        }

        protected override void ReceiveMessage(Messages.Geometry.PointStamped message)
        {
            position = GetPosition(message).Ros2Unity();
            isMessageReceived = true;
        }

        private void ProcessMessage()
        {
            PublishedTransform.position = position;
        }

        private Vector3 GetPosition(Messages.Geometry.PointStamped message)
        {
            //Debug.Log(message.point.x);
            return new Vector3(
                message.point.x,
                message.point.y,
                message.point.z);
        }
    }
}