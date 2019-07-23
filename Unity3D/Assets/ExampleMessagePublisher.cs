
using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class ExampleMessagePublisher : Publisher<Messages.ExampleMessage>
    {
        public string FrameId = "Unity";
        private Messages.ExampleMessage message;

        protected override void Start()
        {
            base.Start();
            InitializeMessage();
        }

        private void FixedUpdate()
        {
            UpdateMessage();
        }

        private void InitializeMessage()
        {
            message = new Messages.ExampleMessage
            {
                arr = new int[100]
            };
        }

        private void UpdateMessage()
        {

            for (int i = 0; i < 100; i++)
            {
                message.arr[i]++;
            }
            Debug.Log(message.arr[2]);
            Publish(message);
        }
    }
}
